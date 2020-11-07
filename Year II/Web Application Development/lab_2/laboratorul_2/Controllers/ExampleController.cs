using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace laboratorul_2.Controllers
{
    public class ExampleController : Controller
    {
        // GET: Example
        public ActionResult Index()
        {
            return View();
        }

        public string Concatenare(string param1, string param2)
        {
            return param1 + param2;
        }

        public string Operatie(int? param1, int? param2, string param3)
        {
            if (param1 == null) return "introduceti primul parametru";
            if (param2 == null) return "introduceti al doulea parametru";
            if (param3 == null) return "introduceti operatia";
            if (param3 != "plus" && param3 != "minus" && param3 != "ori" && param3 != "div") return "operatie invalida";
            else if (param3 == "plus") return param1.ToString() + " + " + param2.ToString() + " = " + (param1 + param2).ToString();
            else if (param3 == "minus") return param1.ToString() + " - " + param2.ToString() + " = " + (param1 - param2).ToString();
            else if (param3 == "ori") return param1.ToString() + " * " + param2.ToString() + " = " + (param1 * param2).ToString();
            else return param1.ToString() + " / " + param2.ToString() + " = " + (param1 / param2).ToString();
        }
    }
}