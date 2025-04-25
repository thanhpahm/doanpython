// Basic JavaScript functions for the library management website

// Function to toggle password visibility
function togglePassword(inputId) {
    const passwordInput = document.getElementById(inputId);
    const toggleIcon = passwordInput.nextElementSibling;

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.classList.remove("fa-eye");
        toggleIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        toggleIcon.classList.remove("fa-eye-slash");
        toggleIcon.classList.add("fa-eye");
    }
}

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;

    let isValid = true;
    const inputs = form.querySelectorAll("input[required]");

    inputs.forEach((input) => {
        if (!input.value.trim()) {
            input.classList.add("error");
            isValid = false;
        } else {
            input.classList.remove("error");
        }
    });

    return isValid;
}

// Device search functionality
function searchDevices() {
    const searchInput = document.getElementById("device-search");
    if (!searchInput) return;

    const searchTerm = searchInput.value.toLowerCase();
    const devices = document.querySelectorAll(".device-card");

    devices.forEach((device) => {
        const deviceName = device
            .querySelector(".device-name")
            .textContent.toLowerCase();
        const deviceInfo = device
            .querySelector(".device-description")
            .textContent.toLowerCase();

        if (
            deviceName.includes(searchTerm) ||
            deviceInfo.includes(searchTerm)
        ) {
            device.style.display = "block";
        } else {
            device.style.display = "none";
        }
    });
}

// Reservation functionality
function reserveDevice(deviceId) {
    // This would be replaced with actual AJAX call in a real implementation
    alert(`Đặt chỗ thiết bị có ID: ${deviceId}`);
    // Update UI to show device is reserved
    const statusElement = document.querySelector(
        `#device-${deviceId} .device-status`
    );
    if (statusElement) {
        statusElement.textContent = "Đã đặt chỗ";
        statusElement.className = "device-status status-reserved";
    }
    // Disable reserve button
    const reserveButton = document.querySelector(
        `#device-${deviceId} .reserve-btn`
    );
    if (reserveButton) {
        reserveButton.disabled = true;
        reserveButton.textContent = "Đã đặt chỗ";
    }
}

// Function to handle tab switching
function openTab(evt, tabId) {
    // Hide all tab content
    const tabContents = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }

    // Remove active class from all tab links
    const tabLinks = document.getElementsByClassName("tab-link");
    for (let i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
    }

    // Show the current tab and add active class to the button
    document.getElementById(tabId).style.display = "block";
    evt.currentTarget.className += " active";
}

// Password strength checker
document.addEventListener("DOMContentLoaded", function () {
    const newPasswordInput = document.getElementById("new-password");
    const confirmPasswordInput = document.getElementById(
        "confirm-new-password"
    );
    const strengthBar = document.querySelector(".strength-bar");
    const passwordMatchMessage = document.querySelector(
        ".password-match-message"
    );

    if (newPasswordInput) {
        newPasswordInput.addEventListener("input", function () {
            const password = this.value;
            let strength = 0;
            let message = "";
            let color = "";

            if (password.length >= 8) strength += 25;
            if (password.match(/[A-Z]/)) strength += 25;
            if (password.match(/[0-9]/)) strength += 25;
            if (password.match(/[^A-Za-z0-9]/)) strength += 25;

            strengthBar.style.width = strength + "%";

            if (strength <= 25) {
                color = "#e74c3c"; // red
                message = "Rất yếu";
            } else if (strength <= 50) {
                color = "#f39c12"; // orange
                message = "Yếu";
            } else if (strength <= 75) {
                color = "#f1c40f"; // yellow
                message = "Trung bình";
            } else {
                color = "#2ecc71"; // green
                message = "Mạnh";
            }

            strengthBar.style.backgroundColor = color;

            // Check if passwords match when both fields have values
            if (confirmPasswordInput.value) {
                checkPasswordsMatch();
            }
        });
    }

    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener("input", checkPasswordsMatch);
    }

    function checkPasswordsMatch() {
        const newPassword = newPasswordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        if (newPassword === confirmPassword && newPassword !== "") {
            passwordMatchMessage.textContent = "Mật khẩu khớp";
            passwordMatchMessage.style.color = "#2ecc71"; // green
        } else {
            passwordMatchMessage.textContent = "Mật khẩu không khớp";
            passwordMatchMessage.style.color = "#e74c3c"; // red
        }
    }

    // Set up form submission handler
    const passwordForm = document.getElementById("change-password-form");
    if (passwordForm) {
        passwordForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const currentPassword =
                document.getElementById("current-password").value;
            const newPassword = document.getElementById("new-password").value;
            const confirmPassword = document.getElementById(
                "confirm-new-password"
            ).value;

            if (!currentPassword || !newPassword || !confirmPassword) {
                alert("Vui lòng điền đầy đủ thông tin");
                return;
            }

            if (newPassword !== confirmPassword) {
                alert("Mật khẩu mới không khớp với xác nhận mật khẩu");
                return;
            }

            // Simulate successful password change
            alert("Đổi mật khẩu thành công!");
            this.reset();
            strengthBar.style.width = "0";
            passwordMatchMessage.textContent = "";
        });
    }

    // Handle account settings form
    const accountSettingsForm = document.getElementById(
        "account-settings-form"
    );
    if (accountSettingsForm) {
        accountSettingsForm.addEventListener("submit", function (e) {
            e.preventDefault();
            alert("Đã lưu thay đổi cài đặt tài khoản!");
        });
    }

    // Set default active tab if on profile page
    const defaultTab = document.getElementById("defaultTab");
    if (defaultTab) {
        defaultTab.click();
    }

    // Set up search functionality
    const searchInput = document.getElementById("device-search");
    if (searchInput) {
        searchInput.addEventListener("keyup", searchDevices);
    }

    // Set up form validation
    const forms = document.querySelectorAll("form");
    forms.forEach((form) => {
        form.addEventListener("submit", function (e) {
            if (!validateForm(form.id)) {
                e.preventDefault();
                alert("Vui lòng điền đầy đủ thông tin bắt buộc!");
            }
        });
    });
});
