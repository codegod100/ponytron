<script>
  export let data;
  import "../app.postcss";
  import ponylog from "$lib/ponylog";
  import { page } from "$app/stores";
  ponylog();
  let pages = ["main", "chats"];
</script>

<div class="grid grid-flow-col auto-cols-max p-2">
  <div class="h1">Ponytron 🐴🤠</div>
  <div>
    {#if data.username && !$page.form}
      <form method="POST" action="/">
        <button
          class="btn variant-filled inline"
          name="username"
          value=""
          type="submit"
          on:click={() => {}}>logout</button
        >
      </form>
    {/if}
  </div>
</div>
{#if data.username}
  <div class="h2"><a href="/profile/{data.username}">{data.username}</a></div>
{/if}

{#if !data.username || $page.form}
  <form method="POST" action="/" class="p-10">
    {#if $page.form}
      <div class="mb-5">Wrong user/pass combo</div>
    {/if}
    Username
    <input name="username" class="input" type="text" />
    Password
    <input name="password" type="password" class="input" />
    <button class="btn variant-filled mt-2">login</button>
  </form>
{/if}

{#if data.username && !$page.form}
  <div class="container">
    <slot />
  </div>

  <div>
    <div class="mb-2">Navigation:</div>
    <!-- <a href="/" class="btn variant-filled">Main</a>
    <a href="/chats" class="btn variant-filled">Chats</a> -->

    <div class="grid grid-flow-col auto-cols-max space-x-1">
      {#each pages as p}
        {#if p != $page.data.nav}
          {#if p == "main"}
            <div><a href="/" class="btn variant-filled">{p}</a></div>
          {:else}
            <div><a href="/{p}" class="btn variant-filled">{p}</a></div>
          {/if}
        {/if}
      {/each}
    </div>
  </div>
{/if}
