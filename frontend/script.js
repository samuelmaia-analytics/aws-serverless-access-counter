const button = document.querySelector("#access-button");
const statusMessage = document.querySelector("#status-message");

async function registerAccess() {
  statusMessage.textContent = "Simulando chamada ao contador...";

  // Substitua por sua URL real do API Gateway quando a infraestrutura for criada.
  const apiUrl = "/contador";

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        source: "coming-soon-page"
      })
    });

    if (!response.ok) {
      throw new Error("Resposta inesperada da API.");
    }

    const data = await response.json();
    statusMessage.textContent = `Acesso registrado. Total atual: ${data.count}.`;
  } catch (error) {
    statusMessage.textContent =
      "Chamada simulada. Configure a URL do API Gateway para usar a integração real.";
  }
}

button.addEventListener("click", registerAccess);
