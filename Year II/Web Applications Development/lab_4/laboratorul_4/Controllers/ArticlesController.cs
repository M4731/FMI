using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Web;
using System.Web.Mvc;
using laboratorul_4.Models;

namespace laboratorul_4.Controllers
{
    public class ArticlesController : Controller
    {
        private ArticleDBContext db = new ArticleDBContext();

        // GET: Articles
        public ActionResult Index()
        {
            var articles = db.Articles.Include("Category");
            ViewBag.Articles = articles;
            return View();
        }

        public ActionResult Show(int id)
        {
            Article article = db.Articles.Find(id);
            ViewBag.Article = article;
            ViewBag.Category = article.Category;
            return View();
        }


        //new - GET - implicit
        public ActionResult New()
        {
            var categories = from cat in db.Categories
                             select cat;
            ViewBag.Categories = categories;
            return View();
        }

        //post
        [HttpPost]
        public ActionResult New(Article article)
        {
            try
            {
                db.Articles.Add(article);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception e)
            {
                return View();
            }
        }

        public ActionResult Edit(int id)
        {
            Article article = db.Articles.Find(id);
            ViewBag.Article = article;
            ViewBag.Category = article.Category;
            var categories = from cat in db.Categories 
                             select cat;
            ViewBag.Categories = categories;
            return View();
        }

        [HttpPut]
        public ActionResult Edit(int id, Article requestArticle)
        {
            try
            {
                Article article = db.Articles.Find(id);
                if (TryUpdateModel(article))
                {
                    article.Title = requestArticle.Title;
                    article.Content = requestArticle.Content;
                    article.Date = requestArticle.Date;
                    article.CategoryId = requestArticle.CategoryId;
                    db.SaveChanges();
                }
                return RedirectToAction("Index");
            }
            catch (Exception e)
            {
                return View();
            }
        }

        [HttpDelete]
        public ActionResult Delete(int id)
        {
            Article article = db.Articles.Find(id);
            db.Articles.Remove(article);
            db.SaveChanges();
            return RedirectToAction("Index");
        }


    }
}