
//
// Pobieranie wierszów ze strony: www.wiersze.co
//
//


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Text.RegularExpressions;
using System.IO;

namespace PoemsCollector
{
    class Program
    {
        static StreamWriter writer;

        static bool FirstLettersAre(string text, string wzorzec)
        {
            if (text.Length < wzorzec.Length) return false;
            for (int x=0; x<wzorzec.Length; x++)
            {
                if (text[x] != wzorzec[x]) return false;
            }
            return true;
        }

        static void DownloadPoemFromWebSite(string webSite)
        {
       //     Console.WriteLine("<startPoem>");
            writer.WriteLine("<startPoem>");

            using (WebClient client = new WebClient())
            {
                client.Encoding = Encoding.GetEncoding("iso-8859-2");
                string htmlCode = client.DownloadString(webSite);
                htmlCode = htmlCode.Split(new string[] { "body" }, StringSplitOptions.None)[1];
                htmlCode = Regex.Replace(htmlCode, @"\r\n?|\n|\t", " ");
                string[] dziwnyPodzial = htmlCode.Split('>');
                dziwnyPodzial = dziwnyPodzial.Skip(1).ToArray();
                int x = 0;
                foreach (string s in dziwnyPodzial)
                {
             
                    if (!FirstLettersAre(s, "<") && !s.Contains("Strona główna"))
                    {
                        string[] kolejnyDziwnySplit = s.Split('<');
                        string linijka = kolejnyDziwnySplit[0];
                        if (linijka.Trim().Length != 0)
                        {
                            linijka = Regex.Replace(linijka, "&nbsp;", "");
                            linijka = linijka.Trim();

                            writer.WriteLine(linijka);
                  //          Console.WriteLine(linijka);

                            if (x == 1)
                            {
                                writer.WriteLine();
                     //           Console.WriteLine();
                            }
                               
                            x++;
                        }
                       
                        if (kolejnyDziwnySplit.Length>1 && kolejnyDziwnySplit[1].ToUpper()=="P" && x>2)
                        {
                            writer.WriteLine();
                //            Console.WriteLine();
                        }
                    }
                    if (s.ToUpper()=="<P" && x>2)
                    {
                        writer.WriteLine();
                    //    Console.WriteLine();
                    }
                    if (s.ToUpper().Contains("ALIGN=RIGHT")&& x>2)
                    {
                        break;
                    }
                        
                }
            //    Console.ReadKey();
            }
          //  Console.WriteLine("<endPoem>");
            writer.WriteLine("<endPoem>");
        }

        static void Main(string[] args)
        {
          //  writer = new StreamWriter(@"D:\project\poems.txt");

            // DownloadPoemFromWebSite("http://wiersze.co/jakmismutno.htm");

            int y = 0;
           // return;
            using (WebClient client = new WebClient())
            {
                string htmlCode = client.DownloadString("http://www.wiersze.co/#2a");
                string wlasciwe = htmlCode.Split(new string[] { "Wiersze polskich autorów" }, StringSplitOptions.None)[1];
                wlasciwe = wlasciwe.Split(new string[] { "Znani i mniej znani w anegdocie" }, StringSplitOptions.None)[0];
                string[] links = wlasciwe.Split(new string[] { "<a href=" }, StringSplitOptions.None);
                foreach(string s in links)
                {
                    
                    if (!FirstLettersAre(s, "https"))
                    {
                        string link = s.Split('>')[0];
                        if (link[0]=='"')
                        {
                            y++;
                            string naprawdeDobryLink = "http://www.wiersze.co/"+link.Trim(new Char[] { '"' });
                            Console.WriteLine(naprawdeDobryLink);
                           // DownloadPoemFromWebSite(naprawdeDobryLink);
                        }
                        
                       
                       // Console.ReadKey();
                    }
                }

            //    Console.WriteLine(htmlCode);
            }
            Console.WriteLine(y);
            Console.ReadKey();
           // writer.Close();


        }
    }
}
