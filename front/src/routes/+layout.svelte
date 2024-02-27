<script>
  export let data;
  import "../app.postcss";
  import ponylog from "$lib/ponylog";

  ponylog();
</script>

<div>
  <div>Ponytron 🐴🤠</div>
  <div>
    {#if data.username}
      <form method="POST" action="/">
        <button name="username" value="" type="submit" on:click={() => {}}
          >logout</button
        >
      </form>
    {/if}
  </div>
</div>

{#if !data.username}
  <form method="POST" action="/">
    Username
    <input name="username" type="text" />
    Password
    <input type="text" />
    <button>login</button>
  </form>
{/if}

{#if data.username}
  <div>
    <slot />
  </div>

  <div>
    <div>Navigation:</div>
    <a href="/">Main</a>
    <a href="/chats">Chats</a>
  </div>
{/if}
