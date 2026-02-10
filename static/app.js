function addAppointment() {
  let patient = document.getElementById("patient").value;
  let doctor = document.getElementById("doctor").value;
  let date = document.getElementById("date").value;

  fetch("/appointments/api/add/", {
    method: "POST",
    body: new URLSearchParams({
      patient: patient,
      doctor: doctor,
      date: date
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("msg").innerText = data.message;
  });
}
