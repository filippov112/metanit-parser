using KnowParser.ViewModels;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace KnowParser.Models
{
    public class SettingsConfig: ViewModel
    {
        private string _Catalog = "C:\\Users\\ilya\\Documents\\KnowParser";
        private string _TextSelector = "div.item.center";
        private List<string> _FilterSelectors = ["h1", "div.date", "div.socBlock", "td.gutter", "style", "div.nav"];
        private string _RequestHeader = "You are an experienced IT instructor and practitioner. I'm providing you with an article on an IT topic. Your task is to create a **complete and structured summary** that **doesn't miss any important information** from the original text. The summary should contain **all key theory and practical templates**, without fluff or unnecessary details.\r\n\r\n### 🎯 CRITICALLY IMPORTANT:\r\n- **DO NOT MISS ANY key details** from the original text\r\n- **DO NOT SKIP limitations, conditions, nuances and features**\r\n- **MAINTAIN information completeness** — better slightly more than to miss something important\r\n- **AVOID information duplication** — even if the original article repeats information, include it only once in your summary\r\n\r\n### Summary Requirements:\r\n\r\n1. **Highlight ALL key definitions** and concepts from the text, using the format:  \r\n    `> ==**Term**== - brief and accurate definition`\r\n\r\n2. **Formulate ALL main properties, limitations, features and nuances** as a bulleted list:  \r\n    `- text` or `- *text*`\r\n\r\n3. **MANDATORILY highlight limitations and conditions** — if the text mentions situations where something works/doesn't work/requires conditions, highlight it with warning formatting:  \r\n    `- <u>⚠️ Limitation: ...</u>` or `- <u>⚠️ Condition: ...</u>`\r\n\r\n4. **Indicate ALL syntax constructs, keywords, parameters** mentioned in the text\r\n\r\n5. **Provide ALL types of examples** mentioned in the text\r\n\r\n6. **Use syntax highlighting** for code (`csharp`, `yaml`, `bash`, `json`, etc.)\r\n\r\n7. **DO NOT OMIT**:\r\n    - Lists of possible values\r\n    - Usage variants\r\n    - Alternative approaches\r\n    - Technical implementation details\r\n\r\n### Examples Requirements:\r\n- **ALL examples must be labeled and commented** (briefly), even if the original text lacks comments\r\n- **Number all examples sequentially**: Ex. 1, Ex. 2, etc.\r\n- **If theory at the beginning of a block is accompanied by examples**, reference them in parentheses: \"Text (ex.1)\"\r\n- **Example format**: `> Ex. 1 - Example title:`\r\n- **Example references in text**: \"Some explanation (ex.1)\"\r\n\r\n### Structure:\r\nOrganize information into **logical blocks** by topics/concepts from the article. In each block:\r\n1. **Theory** — definitions, properties, features (in the format above)\r\n2. **Practice/Examples** — syntax, code, usage methods (if applicable)\r\n\r\n### Section Naming:\r\n- **NO meaningless subsection titles** like \"Theory:\" or \"Practice:\"\r\n- **Theory sections** should have meaningful topic names\r\n- **Practice sections** should have descriptive example titles\r\n\r\n### Markdown Header Standardization:\r\n- **Main topic blocks**: Use `###` (H3 level)\r\n- **Subsections**: Use `#####` or `######` (H5 or H6 level)\r\n- **Add horizontal rule `---` before each `###` header** (except the first one)\r\n\r\n### STRICT Formatting Style Requirements:\r\n1. **`== ==` formatting** — use **ONLY and EXCLUSIVELY** for new terms when giving their definitions\r\n2. **Bold formatting (`**text**`)** — use **ONLY and EXCLUSIVELY** on individual words and phrases in text when you need to emphasize them with stronger intonation (preferably don't overuse)\r\n3. **Underlining (`<u>text</u>`)** — use **SPARINGLY** — only for CRITICAL information that requires reader's attention\r\n\r\n### General Principles:\r\n- MAXIMUM information completeness\r\n- Concise, but without omissions\r\n- Clear and logically structured\r\n- No fluff\r\n- Focused on practical application\r\n- Every important fact from the original must be reflected\r\n- **NO information duplication** — if article repeats something, include it only once\r\n- **ALL examples labeled and commented**\r\n- **MEANINGFUL section titles only**\r\n- **STRICT adherence to formatting style**\r\n\r\n### ⚠️ IMPORTANT:\r\n- **DO NOT ADD final summary, conclusion, or recap section at the end** — this is redundant and duplicates what's already written\r\n- **Write the summary in Russian language**\r\n\r\nHere is the article:\r\n`````";
        private string _RequestFooter = "`````";

        public string Catalog
        {
            get => _Catalog;
            set { _Catalog = value; OnPropertyChanged(); }
        }
        public string TextSelector
        {
            get => _TextSelector;
            set { _TextSelector = value; OnPropertyChanged(); }
        }
        public List<string> FilterSelectors
        {
            get => _FilterSelectors;
            set { _FilterSelectors = value; OnPropertyChanged(); }
        }
        public string RequestHeader
        {
            get => _RequestHeader;
            set { _RequestHeader = value; OnPropertyChanged(); }
        }
        public string RequestFooter
        {
            get => _RequestFooter;
            set { _RequestFooter = value; OnPropertyChanged(); }
        }

        public SettingsConfig CopySettings()
        {
            var json = JsonConvert.SerializeObject(this);
            JsonConvert.DeserializeObject<SettingsConfig>(json);
            var copy = new SettingsConfig();
            JsonConvert.PopulateObject(json, copy);
            return copy;
        }
    }
}
