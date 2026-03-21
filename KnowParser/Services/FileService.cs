using KnowParser.Models;
using System.Diagnostics;
using System.IO;

namespace KnowParser.Services
{
    public class FileService
    {
        public static async Task SaveContent(List<PageData> pages, string catalog, string header, string footer, Action<string>? logger = null)
        {
            foreach (var page in pages)
            {
                AddDirectoryAndFilePath(page, catalog);
                if (!Path.Exists(page.Directory))
                    Directory.CreateDirectory(page.Directory);
                await SaveTo(page.File, header + page.Content + footer, logger);
                logger?.Invoke($"Сохранен файл:{{ Path = {page.File} }}");
            }
        }

        // Сохранить текстовое содержимое в файл
        public static async Task SaveTo(string path, string content, Action<string>? logger = null)
        {
            try
            {
                using StreamWriter writer = new(path);
                await writer.WriteLineAsync(content);
            }
            catch (IOException e)
            {
                logger?.Invoke($"Error writing file: { e.Message}");
            }
        }

        // Создать маршрут сохранения
        public static void AddDirectoryAndFilePath(PageData page, string catalog)
        {
            var relation_address = page.Url.ToLower().Split(page.Domain).Last();
            relation_address = string.Join('/', relation_address.Split('/')[..^1]);
            if (relation_address.StartsWith('/'))
                relation_address = relation_address[1..];
            page.Directory = Path.Combine(catalog, relation_address);
            page.File = Path.Combine(catalog, relation_address, page.Name + ".txt");
        }
    }
}
