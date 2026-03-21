using KnowParser.Models;
using KnowParser.Services;
using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Runtime.CompilerServices;
using System.Text;
using System.Windows;
using System.Windows.Input;

namespace KnowParser.ViewModels
{
    public class SettingsVM: ViewModel
    {
        private string _filteredSelectors = "";

        // Properties
        public string SaveDirectoryPath
        {
            get => _config.Catalog;
            set
            {
                _config.Catalog = value;
                _saveEnabled = true;
                OnPropertyChanged();
            }
        }

        public string TextSelector
        {
            get => _config.TextSelector;
            set
            {
                _config.TextSelector = value;
                _saveEnabled = true;
                OnPropertyChanged();
            }
        }

        public string FilteredSelectors
        {
            get => _filteredSelectors;
            set
            {
                _filteredSelectors = value;
                _saveEnabled = true;
                OnPropertyChanged();
            }
        }

        public string RequestHeader
        {
            get => _config.RequestHeader;
            set
            {
                _config.RequestHeader = value;
                _saveEnabled = true;
                OnPropertyChanged();
            }
        }

        public string RequestFooter
        {
            get => _config.RequestFooter;
            set
            {
                _config.RequestFooter = value;
                _saveEnabled = true;
                OnPropertyChanged();
            }
        }
        private bool _saveEnabled = false;
        private readonly ISettingsManager _SettigsManager;

        private SettingsConfig __config;
        private SettingsConfig _config { 
            get => __config; 
            set {  
                __config = value; 
                SetFilteredSelectorsList(value.FilterSelectors); 
                OnPropertyChanged(); 
            }  
        }

        // Commands
        public ICommand SelectFolderCommand { get; }
        public ICommand SaveCommand { get; }
        public ICommand SaveAsCommand { get; }
        public ICommand ResetCommand { get; }
        public ICommand LoadCommand { get; }

        public SettingsVM(ISettingsManager settginsManager)
        {
            _SettigsManager = settginsManager;
            _config = _SettigsManager.Current;
            SelectFolderCommand = new RelayCommand(ExecuteSelectFolder);
            _saveEnabled = false;
            SaveCommand = new RelayCommand(ExecuteSave, CanSaveSettings);
            SaveAsCommand = new RelayCommand(ExecuteSaveAs, CanSaveSettings);
            ResetCommand = new RelayCommand(ExecuteReset);
            LoadCommand = new RelayCommand(ExecuteLoad);
        }

        #region Command Implementations

        private void ExecuteSelectFolder(object? parameter)
        {
            try
            {
                var dialog = new Microsoft.Win32.OpenFileDialog
                {
                    Title = "Выберите каталог",
                    FileName = "Папка"
                };

                if (dialog.ShowDialog() == true)
                {
                    SaveDirectoryPath = Path.GetDirectoryName(dialog.FileName) ?? "";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка выбора директории: {ex.Message}", "Ошибка");
            }
        }

        private void ExecuteSave(object? parameter)
        {
            try
            {
                _config.FilterSelectors = GetFilteredSelectorsList();
                _SettigsManager.SaveAsync(_config);
                _saveEnabled = false;
                MessageBox.Show("Настройки сохранены успешно!", "Успех", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка сохранения: {ex.Message}", "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void ExecuteSaveAs(object? parameter)
        {
            try
            {
                var dialog = new SaveFileDialog
                {
                    Title = "Сохранить конфигурацию как",
                    Filter = "Файлы конфигурации|*.json;*.xml|Все файлы|*.*"
                };

                if (dialog.ShowDialog() == true)
                {
                    _config.FilterSelectors = GetFilteredSelectorsList();
                    _SettigsManager.SaveAsync(_config, dialog.FileName);
                    _saveEnabled = false;
                    MessageBox.Show("Настройки сохранены успешно!", "Успех", MessageBoxButton.OK, MessageBoxImage.Information);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка сохранения: {ex.Message}", "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private bool CanSaveSettings(object? parameter) => _saveEnabled;

        private void ExecuteReset(object? parameter)
        {
            var result = MessageBox.Show(
                "Вы уверены? Все изменения будут утеряны.",
                "Сброс настроек",
                MessageBoxButton.YesNo,
                MessageBoxImage.Question);

            if (result == MessageBoxResult.Yes)
            {
                _SettigsManager.ResetToDefaults();
                _config = _SettigsManager.Current;
                _saveEnabled = false;
            }
        }

        private void ExecuteLoad(object? parameter)
        {
            try
            {
                var dialog = new OpenFileDialog
                {
                    Title = "Загрузить конфигурацию",
                    Filter = "Файлы конфигурации|*.json;*.xml|Все файлы|*.*"
                };

                if (dialog.ShowDialog() == true)
                {
                    _SettigsManager.LoadAsync(dialog.FileName).Wait();
                    _config = _SettigsManager.Current;
                    _saveEnabled = false;
                    MessageBox.Show("Конфигурация загружена!", "Успех", MessageBoxButton.OK, MessageBoxImage.Information);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка загрузки: {ex.Message}", "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void SetFilteredSelectorsList(List<string> selectors)
        {
            FilteredSelectors = string.Join('\n', selectors);
        }
        private List<string> GetFilteredSelectorsList()
        {
            return FilteredSelectors.Split('\n', StringSplitOptions.RemoveEmptyEntries).ToList();
        }
        #endregion
    }

    
}
