using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using laboratorul_3.Models;

namespace laboratorul_3.Controllers
{
    public class ArticlesController : Controller
    {
        // GET: Articles
        [ActionName("listare")]
        [OutputCache(Duration = 30)]
        public ActionResult Index()
        {
            Article[] articles = GetArticles();

            ViewBag.Articles = articles;

            return View("Index");
        }

        //GET - implicit: vizualizarea unui sg articol
        //[HttpGet]
        public ActionResult Show(int id)
        {
            Article[] articles = GetArticles();

            try 
            {
                ViewBag.Article = articles[id];
                return View();
            }
            catch(Exception e)
            {
                ViewBag.ErrorMessage = e.Message;
                return View("Error");
            }
        }

        //GET - implicit: afis formular de adaugare articolnou
        public ActionResult New()
        {
            return View();
        }

        [HttpPost]
        public ActionResult New(Article article)
        {
            //... cod adaugare articol nou
            return View("NewPostMethod");
        }

        //Get -implicit  :afis datelor unui articol pt editare
        public ActionResult Edit(int id)
        {
            ViewBag.Id = id; 
            return View();
        }

        [HttpPut]
        public ActionResult Edit(Article article)
        {
            //... cod modif articol
            return View("EditPutMethod");
        }

        [HttpDelete]
        public ActionResult Delete(int id)
        {
            //... cod stergere articol
            return View("DeleteMethod");
        }

        [NonAction]
        public Article[] GetArticles()
        {
            // Instantiem un array de articole
            Article[] articles = new Article[3];

            // Cream articole
            for (int i = 0; i < 3; i++)
            {
                Article article = new Article();
                article.Id = i;
                article.Title = "Articol " + (i + 1).ToString();
                article.Content = "Continut articol " + (i + 1).ToString();
                article.Date = DateTime.Now;

                // Adaugam articolul in array
                articles[i] = article;
            }
            return articles;
        }
    }
}