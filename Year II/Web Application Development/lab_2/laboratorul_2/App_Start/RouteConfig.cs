using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace laboratorul_2
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                 name: "Concatenare",
                 url: "concatenare/{param1}/{param2}",
                 defaults: new
                             {
                                 controller = "Example",
                                 action = "Concatenare",
                                 param1 = UrlParameter.Optional,
                                 param2 = UrlParameter.Optional
                             }
                );

            routes.MapRoute(
                 name: "Operatie",
                 url: "operatie/{param1}/{param2}/{param3}",
                 defaults: new
                             {
                                 controller = "Example",
                                 action = "Operatie",
                                 param1 = UrlParameter.Optional,
                                 param2 = UrlParameter.Optional,
                                 param3 = UrlParameter.Optional
                 }
                );

            routes.MapRoute(
                name: "StudentIndex",
                url: "students/all",
                defaults: new { controller = "Student", action = "Index" }
             );
            routes.MapRoute(
                name: "StudentNew",
                url: "students/new",
                defaults: new { controller = "Student", action = "Create" }
            );
            routes.MapRoute(
                name: "StudentShow",
                url: "students/{id}/show",
                defaults: new { controller = "Student", action = "Show", id = UrlParameter.Optional }
            );
            routes.MapRoute(
                name: "StudentEdit",
                url: "students/{id}/edit",
                defaults: new { controller = "Student", action = "Edit", id = UrlParameter.Optional }
            );
            routes.MapRoute(
                name: "StudentDelete",
                url: "students/{id}/delete",
                defaults: new { controller = "Student", action = "Delete", id = UrlParameter.Optional }
            );

            // aceasta ruta permite accesarea metodei doar in momentul in care exista un numar CORECT de telefon
            routes.MapRoute(
                name: "SearchTelefon",
                url: "search/telefon/{telef}",
                defaults: new { controller = "Search", action = "NumarTelefon", telef = UrlParameter.Optional },
                constraints: new { telef = @"^[0][0-9]{9}$" }
            );

            // constrangerea nu trebuie sa fie atat de restrictiva incat sa nu permita accesarea metodei
            routes.MapRoute(
                name: "CautareTelefon",
                url: "cautare/telefon/{telef}",
                defaults: new { controller = "Search", action = "NumarTelefon", telef = UrlParameter.Optional },
                constraints: new { telef = @"[0-9]*$" }
            );

            // Intra pe ruta default deoarece exista controller Search cu actiune CNP, iar pentru parametrul
            // CNP, cand nu trece de expresia regulata din ruta nu se ia in calcul ruta aceasta
            routes.MapRoute(
                name: "SearchCNP",
                url: "search/cnp/{cnp}",
                defaults: new { controller = "Search", action = "CNP", cnp = UrlParameter.Optional },
                constraints: new { cnp = @"^[1256][0-9]{12}$" }
            );

            // Ruta corecta
            routes.MapRoute(
                name: "CautareCNP",
                url: "search/cautarecnp/{cnp}", // s-a modificat parametrul de control astfel incat sa nu se potriveasca cu actiunea din controller
                defaults: new { controller = "Search", action = "CNP", cnp = UrlParameter.Optional },
                constraints: new { cnp = @"[0-9]*$" }
            );

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
            );
        }
    }
}
