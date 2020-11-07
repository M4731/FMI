using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace laboratorul_2.Controllers
{
    public class SearchController : Controller
    {
        // GET: Search
        public ActionResult Index()
        {
            return View();
        }

        public string NumarTelefon(string telef)
        {
            if (telef == null)
            {
                return "Introduceti numarul de telefon";
            }

            if (telef.Length < 10)
                return "Numarul de telefon nu are suficiente cifre";

            else if (telef.Length > 10)
                return "Numarul de telefon are prea multe cifre";
            else
                return "Cautare pentru nr de telefon: " + telef;


        }

        public string CNP(string cnp)
        {
            if (cnp == null)
            {
                return "Introduceti CNP";
            }
            String first_letter = cnp.Substring(0, 1);
            if (first_letter == "1" || first_letter == "2" || first_letter == "5" || first_letter == "6")
            {
                if (cnp.Length == 13)
                {
                    return "Cautare pentru CNP: " + cnp;
                }
                else
                {
                    return "Lungima CNP invalida";
                }
            }
            else
            {
                return "CNP Invalid";
            }
        }
    }
}