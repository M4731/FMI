using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace laboratorul_4.Models
{
    public class Article
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public string Title { get; set; }
        [Required]
        public string Content { get; set; }
        public DateTime Date { get; set; }

        //cheia externa
        public int CategoryId { get; set; }

        //unde refera cheia externa
        public virtual Category Category { get; set; }

        public virtual ICollection<Comment> Comments { get; set; }
    }

}


