using Microsoft.AspNetCore.Mvc;

namespace ThưQuánSV.Controllers
{
    public class AccountController : Controller
    {
        public IActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Login(string username, string password, bool remember)
        {
            // Xử lý đăng nhập ở đây
            return RedirectToAction("Profile");
        }

        public IActionResult Register()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Register(string fullname, string student_id, string email,
                                     string phone, string password, string confirm_password,
                                     bool terms)
        {
            // Xử lý đăng ký ở đây
            return RedirectToAction("Login");
        }

        public IActionResult ForgotPassword()
        {
            return View();
        }

        public IActionResult Profile()
        {
            return View();
        }
    }
}