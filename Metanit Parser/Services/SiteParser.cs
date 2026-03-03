using AngleSharp;

namespace Metanit_Parser.Services
{
    public class SiteParser
    {
        /// <summary>
        /// Собирает релевантный текст страницы
        /// </summary>
        /// <param name="url"></param>
        /// <param name="selector"></param>
        /// <param name="filter_selectors"></param>
        /// <returns></returns>
        public async Task<string[]> Parse(string url, string selector, string[] filter_selectors)
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
            return [.. elements.Select(e => e.TextContent)];
        }

        /// <summary>
        /// Собирает оглавление
        /// </summary>
        /// <param name="url"></param>
        /// <param name="a_selector"></param>
        /// <returns></returns>
        public async Task<List<(string Title, string Link)>> ParseLinks(string url, string a_selector)
        {
            var config = Configuration.Default.WithDefaultLoader();
            var context = BrowsingContext.New(config);
            var document = await context.OpenAsync(url);

            var tags_a = document.QuerySelectorAll(a_selector);
            List<(string Title, string Link)> links = [];
            foreach (var tag in tags_a)
            {
                var title = tag.TextContent;
                var link = url + tag.GetAttribute("href");
                links.Add((title, link));
            }
            return links;
        }
    }
}
