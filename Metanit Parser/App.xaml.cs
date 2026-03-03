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
            var parser = new Services.SiteParser();

            var content = parser.Parse("https://metanit.com/java/android/18.1.php", "div.item.center", ["h1", "div.date", "div.socBlock", "td.gutter", "style", "div.nav"]);

            Debug.Write(string.Join("\n", content.Result[0].Split("\n").Select(s => s.Trim()).Where(s => !string.IsNullOrEmpty(s))));


        }
    }

}
