using KnowParser.Models;
using Newtonsoft.Json;
using System.IO;
using Formatting = Newtonsoft.Json.Formatting;

namespace KnowParser.Services
{
    public interface ISettingsManager
    {
        public SettingsConfig Current { get; }
        public Task LoadAsync(string? filePath = null);
        public Task SaveAsync(SettingsConfig config, string? path = null);
        public Task ResetToDefaults();
    }
    public class SettingManager: ISettingsManager
    {
        private readonly string _filePath;
        private SettingsConfig _current = new();
        public SettingsConfig Current { get => _current.CopySettings(); private set { _current = value.CopySettings(); } }

        // Существующий конструктор для production
        public SettingManager() : this(null) { }

        // Конструктор для тестирования
        public SettingManager(string? customFilePath)
        {
            _filePath = customFilePath ?? GetDefaultPath();
            LoadAsync(_filePath);
        }

        private static string GetDefaultPath()
        {
            var appData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            var dir = Path.Combine(appData, "KnowParser");
            if (!Directory.Exists(dir)) Directory.CreateDirectory(dir);
            return Path.Combine(dir, "settings.json");
        }

        public async Task LoadAsync(string? filePath = null)
        {
            filePath = filePath ?? _filePath;
            await Task.Run(() =>
            {
                if (File.Exists(filePath))
                {
                    try
                    {
                        var json = File.ReadAllText(filePath);
                        var settings = JsonConvert.DeserializeObject<SettingsConfig>(json);
                        if (settings != null)
                            Current = settings;
                    }
                    catch
                    {
                        // При ошибке чтения используем настройки по умолчанию
                        Current = new SettingsConfig();
                    }
                }
            });
        }

        public async Task SaveAsync(SettingsConfig config, string? path = null)
        {
            await Task.Run(() =>
            {
                try
                {
                    var json = JsonConvert.SerializeObject(config, Formatting.Indented);
                    File.WriteAllText(path ?? _filePath, json);
                    Current = config;
                }
                catch (Exception ex)
                {
                    // Логирование ошибки сохранения
                    System.Diagnostics.Debug.WriteLine($"Settings save error: {ex.Message}");
                }
            });
        }

        public async Task ResetToDefaults()
        {
            await SaveAsync(new());
        }
    }
}
