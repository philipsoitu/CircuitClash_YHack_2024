<script>
    export let inputData = [];
    export let outputData = [];
    export let truthTable = [];
  </script>
  
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
    }
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: center;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
  
  <table>
    <thead>
      <tr>
        <th colspan="{inputData.length}">INPUT</th>
        <th colspan="{outputData.length}">OUTPUT</th>
      </tr>
      <tr>
        {#each inputData as input}
          <th>{input}</th>
        {/each}
        {#each outputData as output}
          <th>{output}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each truthTable as row}
        <tr>
          {#each inputData as input}
            <td>{row[input]}</td>
          {/each}
          {#each outputData as output}
            <td>{row[output]}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
  