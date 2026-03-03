using System.Net.Http;

namespace Metanit_Parser.Services
{
    public class LLMClient
    {
        private readonly HttpClient _httpClient;
        private readonly string _baseUrl;

        public LLMClient(string baseUrl = "http://localhost:11434")
        {
            _baseUrl = baseUrl.TrimEnd('/');
            _httpClient = new HttpClient
            {
                Timeout = TimeSpan.FromMinutes(5)
            };
        }
    }
}
