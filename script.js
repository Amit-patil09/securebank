loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {

        const response = await fetch("https://securebank-ze8e.onrender.com/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

      if (data.success) {

    displayUsername.textContent = username;

    document.getElementById("balance").textContent =
        data.balance.toLocaleString("en-IN", {
            minimumFractionDigits: 2
        });

    loginPage.style.display = "none";
    dashboard.style.display = "block";
} else {

            alert(data.message);

        }

    } catch (error) {

        alert("Cannot connect to the bank server.");

        console.error(error);
    }
});