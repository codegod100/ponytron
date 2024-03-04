<script>
  export let data;
  import "../app.postcss";
  import ponylog from "$lib/ponylog";
  import { page } from "$app/stores";
  console.log("page form", $page.form);
  ponylog();
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

<form method="POST" action="/" class="p-10">
  {#if $page.form}
    <div class="mb-5">Wrong user/pass combo</div>
  {/if}
  {#if !data.username || $page.form}
    Username
    <input name="username" class="input" type="text" />
    Password
    <input name="password" type="password" class="input" />
    <button class="btn variant-filled mt-2">login</button>
  {/if}
</form>

{#if data.username && !$page.form}
  <div class="container">
    <slot />
  </div>

  <div>
    <div class="mb-2">Navigation:</div>
    <a href="/" class="btn variant-filled">Main</a>
    <a href="/chats" class="btn variant-filled">Chats</a>
  </div>
{/if}
