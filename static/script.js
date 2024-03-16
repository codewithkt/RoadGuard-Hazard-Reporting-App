document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('hazardForm');
    const hazardReportsDiv = document.getElementById('hazardReports');
  
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const formData = new FormData(form);
      const response = await fetch('/submit_hazard', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        form.reset();
        alert('Hazard report submitted successfully!');
        loadHazardReports();
      } else {
        alert('Failed to submit hazard report.');
      }
    });
  
    async function loadHazardReports() {
      const response = await fetch('/get_hazard_reports');
      const data = await response.json();
      const hazardReports = data.hazard_reports;
  
      const reportsHTML = hazardReports.map((report) => {
        return `
          <div class="hazard-report">
            <h3>Location: ${report.location}</h3>
            <p>Type: ${report.type}</p>
            <p>Description: ${report.description}</p>
          </div>
        `;
      }).join('');
  
      hazardReportsDiv.innerHTML = reportsHTML;
    }
  
    loadHazardReports();
  });
  