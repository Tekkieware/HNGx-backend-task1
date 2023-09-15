<h1>User API Documentation</h1>
<h5>Base URL: https://hngx-bac-task1.onrender.com</h5>

<ol>
  <li>
    <h1>Create a New Person</h1>
    <ul>
      <li><h5>Endpoint: `/api`</h5></li>
      <li><h5>HTTP Method: POST</h5></li>
      <li><h5>Request Body:</h5></li>
      <code>{
  "name": "James Madison",
  "email": "James@gmail.com",
  "country": "Nigeria"
}</code>
      <li><h5>Response</h5></li>
      <ul>
        <li><h5>HTTP Status Code: 201 Created</h5></li>
        <li><h5>Response Body:</h5></li>
      <code>{
        "id": 4,
  "name": "James Madison",
  "email": "James@gmail.com",
  "country": "Nigeria"
}</code>
      </ul>
    </ul>
  </li>

</ol>


