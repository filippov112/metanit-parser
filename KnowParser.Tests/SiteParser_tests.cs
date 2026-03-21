using KnowParser.Services;

namespace KnowParser.Tests
{
    public class SiteParser_tests
    {
        [Theory]
        [InlineData("https://www.google.com/search?q=MsTest&oq=MsTest&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE1NjBqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8", "https://www.google.com")]
        [InlineData("www.google.com/search?q=MsTest&oq=MsTest&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE1NjBqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8", "www.google.com")]
        [InlineData("www.google.com", "www.google.com")]
        [InlineData("www.GOOGLE.com", "www.google.com")]
        public void GetDomain(string url, string result)
        {
            // Assert
            Assert.Equal(SiteParser.GetDomain(url), result);
        }

        [Theory]
        [InlineData("https://metanit.com/web/javascript/28.1.php", "https://metanit.com", "https://metanit.com/web/javascript/28.1.php")]
        [InlineData("28.1.php", "https://metanit.com", "https://metanit.com/28.1.php")]
        [InlineData("https://icons8.com/icons/collections/qzl7dpik5gtdrm7fxl08--style-fluency", "https://metanit.com", "https://icons8.com/icons/collections/qzl7dpik5gtdrm7fxl08--style-fluency")]
        [InlineData("http://metanit.com/web/javascript/28.1.php", "http://metanit.com", "http://metanit.com/web/javascript/28.1.php")]
        [InlineData("http://meTANIT.com/web/javascript/28.1.php", "http://metanit.com", "http://metanit.com/web/javascript/28.1.php")]
        public void GetFullUrl(string url, string domain, string result)
        {
            // Assert
            Assert.Equal(SiteParser.GetFullUrl(url, domain), result);
        }

        [Theory]
        [InlineData("metanit.com/python/", "metanit.com", "metanit.com/python/pandas/9.1.php", true, true)]
        [InlineData("metanit.com/python/", "metanit.com", "metanit.com/python__/pandas/9.1.php", true, false)]
        [InlineData("metanit.com/python/", "metanit.com", "metanit.com/python__/pandas/9.1.php", false, true)]
        [InlineData("metanit.com/python/", "metanit.com", "https://yoomoney.ru/to/410011174743222", true, false)]
        [InlineData("metanit.com/python/", "metanit.com", "https://yoomoney.ru/to/410011174743222", false, false)]
        [InlineData("metanit.com/python/", "metanit.com", "https://metanit.com/python/pandas/9.1.php", true, true)]
        [InlineData("metanit.com/python/", "metanit.com", "https://metanit.com/python/pandas/9.1.php", false, true)]
        public void IsTrueLink(string startLink, string domain, string url, bool onlyChildren, bool result)
        {
            // Assert
            Assert.Equal(SiteParser.IsTrueLink(startLink, domain, url, onlyChildren), result);
        }
    }
}
