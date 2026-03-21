using KnowParser.Services;
using System.Diagnostics;
using System.Windows;

namespace Metanit_Parser
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        public App()
        {
            //var parser = new SiteParser();

            //var content = SiteParser.GetText(, "div.item.center", ["h1", "div.date", "div.socBlock", "td.gutter", "style", "div.nav"]);

            //Debug.Write(string.Join("\n", content.Result[0].Split("\n").Select(s => s.Trim()).Where(s => !string.IsNullOrEmpty(s))));

            var pages = SiteParser.ParseSite("https://metanit.com/sharp/grpc/", true).Result;
            FileService.SaveContent(pages, "C:\\Users\\ilya\\Desktop\\gRPC");
        }
    }

}
