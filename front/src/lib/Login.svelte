<script>
  import { storedname, create_user } from "$lib/common";
  import { css } from "styled-system/css";
  export let logged_in = false;
  export let username = $storedname;
  let password = "";

  if (username) {
    logged_in = true;
  }
</script>

{#if !logged_in}
  <form
    on:submit|preventDefault={async () => {
      storedname.set(username);
      await create_user({ username, password });
      logged_in = true;
    }}
  >
    Username
    <input
      bind:value={username}
      type="text"
      class={css({ background: "amber.500", rounded: "md", p: 2 })}
    />
    Password
    <input
      bind:value={password}
      type="text"
      class={css({ background: "amber.500", rounded: "md", p: 2 })}
    />
    <button class={css({ bg: "amber.500", rounded: "md", p: 2 })}>login</button>
  </form>
{:else}
  Hello {username}
  <button
    class={css({ bg: "amber.500", rounded: "md", p: 2 })}
    on:click={() => {
      logged_in = false;
      storedname.set("");
    }}>logout</button
  >
{/if}
<div>&nbsp;</div>
