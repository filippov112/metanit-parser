using AngleSharp;
using KnowParser.Models;

namespace KnowParser.Services
{
    public class SiteParser
    {
        public static async Task<List<PageData>> ParseSite(string startLink, bool onlyChildren)
        {
            startLink = startLink.ToLower();
            var domain = GetDomain(startLink);
            List<PageData> pages = await GetLinks(startLink, domain, onlyChildren);

            foreach (var page in pages)
            {
                page.Content = await GetText(page.Url, "div.item.center", ["h1", "div.date", "div.socBlock", "td.gutter", "style", "div.nav"]);
            }
            return pages;
        }


        /// <summary>
        /// Собирает релевантный текст страницы
        /// </summary>
        /// <param name="url"></param>
        /// <param name="selector"></param>
        /// <param name="filter_selectors"></param>
        /// <returns></returns>
        public static async Task<string> GetText(string url, string selector, string[] filter_selectors)
        {
            var config = Configuration.Default.WithDefaultLoader();
            var context = BrowsingContext.New(config);
            var document = await context.OpenAsync(url);

            var elements = document.QuerySelectorAll(selector);
            foreach (var element in elements)
            {
                foreach (var filter_selector in filter_selectors)
                {
                    var trash = element.QuerySelectorAll(filter_selector);
                    foreach (var trash_element in trash)
                    {
                        trash_element.Remove();
                    }
                }
            }
            return string.Join("\n", elements.Select(e => e.TextContent).Select(s => string.IsNullOrEmpty(s.Trim()) ? s.Trim() : s).Where(s => !string.IsNullOrEmpty(s)));
        }

        /// <summary>
        /// Собирает оглавление
        /// </summary>
        /// <param name="startLink"></param>
        /// <returns></returns>
        public static async Task<List<PageData>> GetLinks(string startLink, string domain, bool onlyChildren)
        {
            var config = Configuration.Default.WithDefaultLoader();
            var context = BrowsingContext.New(config);
            var document = await context.OpenAsync(startLink);

            var tags_a = document.QuerySelectorAll("a");
            List<PageData> links = [];
            foreach (var tag in tags_a)
            {
                var title = tag.TextContent;
                var link = tag.GetAttribute("href");
                if (!string.IsNullOrEmpty(link) && link != "/")
                {
                    link = GetFullUrl(link, startLink);
                    if (IsTrueLink(startLink, domain, link, onlyChildren))
                        links.Add(new() { Name = title, Url = link, Domain = domain });
                }
            }
            return links;
        }

        // Соответствует ли ссылка критериям поиска
        public static bool IsTrueLink(string startLink, string domain, string url, bool onlyChildren)
        {
            return (!onlyChildren && url.Contains(domain)) || url.Contains(startLink);
        }


        // Получает домен сайта
        public static string GetDomain(string url)
        {
            url = url.ToLower();
            var protocol_and_adress = url.Split("://");
            var domain = protocol_and_adress.Last().Split("/").First();
            if (protocol_and_adress.Length > 1)
                domain = protocol_and_adress.First() + "://" + domain;
            return domain;
        }

        // Абсолютный путь
        public static string GetFullUrl(string url, string domain)
        {
            url = url.ToLower();
            if (url.Contains("//"))
                return url;
            if (url.StartsWith('/'))
                url = url[1..];
            return domain + "/" + url;
        }    
    }
}
