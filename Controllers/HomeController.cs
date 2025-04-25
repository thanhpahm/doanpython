using Microsoft.AspNetCore.Mvc;

namespace ThưQuánSV.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Devices()
        {
            return View();
        }
    }
}