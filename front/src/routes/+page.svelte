<script>
  export let data;
</script>

<div>
  Hello {data.username} 🐼!
</div>

<h2>Social</h2>

<div>Users:</div>

{#each data.users as user}
  <div>
    Username: {user.username}
  </div>
{/each}
