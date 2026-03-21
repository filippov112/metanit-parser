using KnowParser.Models;
using System.Diagnostics;
using System.IO;

namespace KnowParser.Services
{
    public class FileService
    {
        public static void SaveContent(List<PageData> pages, string catalog)
        {
            foreach (var page in pages)
            {
                AddDirectoryAndFilePath(page, catalog);
                if (!Path.Exists(page.Directory))
                    Directory.CreateDirectory(page.Directory);
                SaveTo(page.File, page.Content);
            }
        }

        // Сохранить текстовое содержимое в файл
        public static void SaveTo(string path, string content)
        {
            try
            {
                using StreamWriter writer = new(path);
                writer.WriteLine(content);
                Debug.WriteLine($"""Сохранен файл "{path}"!""");
            }
            catch (IOException e)
            {
                Debug.WriteLine("Error writing file: {0}", e.Message);
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
