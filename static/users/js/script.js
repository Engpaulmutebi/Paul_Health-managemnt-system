// Wait for the DOM to fully load before running the script
document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript is loaded and running!");

  // Example: Add event listener for form submission
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent form from submitting normally

      // Log form data or any actions you want to perform on form submission
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      console.log("Email:", email);
      console.log("Password:", password);

      // Example: Display an alert after form submission
      alert("Form submitted with email: " + email);
    });
  }

  // Example: Handling checkbox state change
  const checkbox = document.getElementById("check_example");
  if (checkbox) {
    checkbox.addEventListener("change", function () {
      if (this.checked) {
        console.log("Checkbox checked!");
      } else {
        console.log("Checkbox unchecked!");
      }
    });
  }
});
