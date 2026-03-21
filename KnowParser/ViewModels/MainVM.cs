using KnowParser.Services;
using KnowParser.Views;
using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Input;

namespace KnowParser.ViewModels
{
    public class MainVM: ViewModel
    {
        public ICommand OpenSettingCommand { get; }
        public ICommand BeginSearchCommand { get; }
        private string _url = "";
        private bool _onlyChildren = true;
        private string _log = "";
        public string Log { get => _log; set { _log = value; OnPropertyChanged(); } }
        public string URL { get => _url; set { _url = value; OnPropertyChanged(); } }
        public bool ScanningFullSite { get => !_onlyChildren; set { _onlyChildren = !value; OnPropertyChanged();  }  }
        public MainVM()
        {
            OpenSettingCommand = new RelayCommand(OpenSettings);
            BeginSearchCommand = new RelayCommand(BeginSearch);
        }


        private async void BeginSearch()
        {
            Log = "";
            await Task.Run(async () => {
                var config = new SettingManager().Current;
                var pages = await SiteParser.ParseSite(URL, _onlyChildren, config.TextSelector, config.FilterSelectors, AddLog);
                await FileService.SaveContent(pages, config.Catalog, config.RequestHeader, config.RequestFooter, AddLog);
            });
        }

        private void OpenSettings(object? parameter)
        {
            var settgins = new SettingsWindow(new(new SettingManager()));
            settgins.ShowDialog();
        }

        private void AddLog(string message)
        {
            Log += string.Join("\n", [Log, message]);
        }
    }
}
