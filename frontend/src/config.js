const config = {
    apiBaseUrl: "http://127.0.0.1:8000", // Backend API URL
    apiEndpoints: {
      clients: "/clients",
      employees: "/employees",
      companies: "/companies",
    },
    // Μπορείς να προσθέσεις επιπλέον ρυθμίσεις αν χρειάζεται:
    timeout: 5000, // Χρόνος timeout για αιτήματα
    headers: {
      "Content-Type": "application/json",
    },
  };
  
  export default config;
  