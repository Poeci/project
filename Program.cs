using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

enum CONNECTION_TYPE {normal, komma, dot, newLine, threedot, question, exclamation, dash, twodot, semicolon}

namespace PoemsToGraph
{
    class Program
    {
        const string START = "<startPoem>";
        const string END = "<endPoem>";
        static StreamReader reader;
        static StreamWriter writer;
        static Dictionary<string, int> dic = new Dictionary<string, int>();
        static int dicIndex = 0;

        static void SkipLines(int count)
        {
            for (int x = 0; x < count; x++)
            {
                reader.ReadLine();
            }
        }

        static void WriteEdge(string word1, string word2, CONNECTION_TYPE type)
        {
            word1 = RemoveInterpunction(word1.ToLower());
            word2 = RemoveInterpunction(word2.ToLower());
            if (!dic.ContainsKey(word1))
            {
                dic[word1] = dicIndex++;
            }
            if (!dic.ContainsKey(word2))
            {
                dic[word2] = dicIndex++;
            }
            /* edges += dic[word1] + " ";

             edges += dic[word2] + " ";
             edges += Array.IndexOf(Enum.GetValues(type.GetType()), type);
             edges += Environment.NewLine;*/

            writer.Write(dic[word1] + " ");

            writer.Write(dic[word2] + " ");
            writer.WriteLine(Array.IndexOf(Enum.GetValues(type.GetType()), type));
            //  Console.ReadKey();
        }

        static bool IsInterpunctionChar(char c)
        {
            if (c == ',') return true;
            if (c == '.') return true;
            if (c == '?') return true;
            if (c == '!') return true;
            if (c == '-') return true;
            if (c == ':') return true;
            if (c == ';') return true;
            return false;
        }

        static string RemoveInterpunction(string word)
        {
            word = word.Replace(",", "");
            word = word.Replace(".", "");
            word = word.Replace("?", "");
            word = word.Replace("!", "");
            word = word.Replace("-", "");
            word = word.Replace(":", "");
            word = word.Replace(";", "");
            word = word.Replace("(", "");
            word = word.Replace(")", "");
            word = word.Replace("\"", "");
            word = word.Replace("\'", "");
            return word;
        }

        static void WriteAllWords()
        {
            foreach (KeyValuePair<string, int> pair in dic)
            {
                /* wordsDic += pair.Value + " ";
                 wordsDic += pair.Key;
                 wordsDic += Environment.NewLine;*/
                writer.Write(pair.Value + " ");
                writer.WriteLine(pair.Key);
            }
        }


        static void WriteAllTypes()
        {
            int p = 0;
            foreach (CONNECTION_TYPE val in Enum.GetValues(typeof(CONNECTION_TYPE)))
            {
                writer.Write((p++).ToString() + " ");
                writer.WriteLine(val.ToString());
            }
        }


        static CONNECTION_TYPE GetConnectionType(string word)
        {
            // todo: newLine
            // todo: dash
            int x = word.Length - 1;
            if (word.Length < 2) return CONNECTION_TYPE.normal;
            if (word[x] == '.' && word[x-1]=='.') return CONNECTION_TYPE.threedot;
            if (word[x] == ',') return CONNECTION_TYPE.komma;
            if (word[x] == '.') return CONNECTION_TYPE.dot;
            if (word[x] == '?') return CONNECTION_TYPE.question;
            if (word[x] == '!') return CONNECTION_TYPE.exclamation;
            if (word[x] == '-') return CONNECTION_TYPE.dash;
            if (word[x] == ':') return CONNECTION_TYPE.twodot;
            if (word[x] == ';') return CONNECTION_TYPE.semicolon;
            return CONNECTION_TYPE.normal;
        }

        static void Main(string[] args)
        {
            reader = new StreamReader(@"D:\poems.txt");
            writer = new StreamWriter(@"D:\graph.txt");
            string lastWordInPreviousLine = null;
            while (reader.Peek()>=0)
            {
                string line = reader.ReadLine();
                if (line==START || line==END)
                {
                    SkipLines(3);
                    continue;
                }
                string[] words = line.Split(' ');
                if (words.Length == 1) continue;
                if (lastWordInPreviousLine!=null)
                {
                    WriteEdge(lastWordInPreviousLine, words[0], CONNECTION_TYPE.newLine);
                }
                for (int x=0; x<words.Length-1; x++)
                {
                    string word = words[x];
                    if (word == "-") continue;
                    string nextWord = words[x+1];
                    if (nextWord == "-" && x+2<words.Length) nextWord = words[x + 2];
                    CONNECTION_TYPE type = GetConnectionType(word);
                    WriteEdge(word, nextWord, type);
                }
                lastWordInPreviousLine = words[words.Length - 1];
                if (lastWordInPreviousLine == "-") lastWordInPreviousLine = null;
            }


            writer.WriteLine("<END>");
            WriteAllWords();
            writer.WriteLine("<TYPES>");
            WriteAllTypes();



            writer.Close();
        }
    }
}
