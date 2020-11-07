using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace laboratorul_2.Controllers
{
    public class StudentController : Controller
    {
        // GET: Student
        public string Index()
        {
            return "Lista tuturor studentilor";
        }

        public string Create()
        {
            return "Formular adaugare student nou";
        }

        public string Show(int? id)
        {
            return "Afisare student cu ID: " + id.ToString();
        }

        public string Edit(int? id)
        {
            return "Editare student cu ID: " + id.ToString();
        }

        public string Delete(int? id)
        {
            return "Stergere student cu ID: " + id.ToString();
        }
    }
}