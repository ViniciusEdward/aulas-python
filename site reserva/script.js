document.getElementById('formReserva').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio real do formulário

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const dataCheckIn = document.getElementById('dataCheckIn').value;
    const dataCheckOut = document.getElementById('dataCheckOut').value;

    alert(`Reserva Confirmada!\nNome: ${nome}\nEmail: ${email}\nCheck-in: ${dataCheckIn}\nCheck-out: ${dataCheckOut}`);
});