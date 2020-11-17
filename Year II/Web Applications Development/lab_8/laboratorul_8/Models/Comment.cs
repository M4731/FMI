using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using laboratorul_8.Models;

namespace Laborator5App.Models
{
    public class Comment
    {
        [Key]
        public int CommentId { get; set; }
        [Required(ErrorMessage = "Campul nu poate fi necompletat")]
        public string Content { get; set; }
        public DateTime Date { get; set; }
        public int ArticleId { get; set; }

        public virtual Article Article { get; set; }

        public string UserId { get; set; }
        public virtual ApplicationUser User { get; set; }
    }
}