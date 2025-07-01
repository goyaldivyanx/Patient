const BASE_URL = "const BASE_URL = https://cors-anywhere.herokuapp.com/https://patient-zdg8.onrender.com";

function showOutput(data) {
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = JSON.stringify(data, null, 2);
}

async function getAllPatients() {
  const res = await fetch(`${BASE_URL}/allpatient`);
  const data = await res.json();
  showOutput(data);
}

async function getPatientById() {
  const id = document.getElementById("patientId").value;
  if (!id) return alert("Please enter a patient ID");
  const res = await fetch(`${BASE_URL}/patient/${id}`);
  const data = res.ok ? await res.json() : { error: "Patient not found" };
  showOutput(data);
}

async function getSortedPatients() {
  const sortBy = document.getElementById("sortField").value;
  const order = document.getElementById("sortOrder").value;
  const res = await fetch(`${BASE_URL}/sorted_data?sort_by=${sortBy}&order=${order}`);
  const data = await res.json();
  showOutput(data);
}
