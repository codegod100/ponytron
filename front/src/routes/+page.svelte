<script>
  export let form;
  export let data;
  console.log(form);
  if (form?.incorrect) {
    delete data.username;
  }
</script>

<div>
  Hello {data.username} 🐼!
</div>

<h2>Social</h2>

<div>Users:</div>

{#each data.users as user}
  <div>
    Username: <a href="/profile/{user.username}">{user.username}</a>
  </div>
{/each}
