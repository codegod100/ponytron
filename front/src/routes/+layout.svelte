<script>
  import Login from "$lib/Login.svelte";
  export let data;
  console.log("layout data", data);
  import { storedname, create_user } from "$lib/common";
  import "../app.css";
  import { css } from "styled-system/css";
  import { container, hstack } from "styled-system/patterns";
  import { PUBLIC_API } from "$env/static/public";
  import { Manager } from "socket.io-client";
  const manager = new Manager(PUBLIC_API);
  const socket = manager.socket("/");
  // console.log("socket", socket);
  socket.io.on("ping", () => {
    console.log("ping from server");
  });
  socket.on("connect", () => {
    // ...
    console.log("socket connected");
  });
  import ponylog from "$lib/ponylog";
  ponylog();
  export let logged_in = false;
  export let username = $storedname;
  let password = "";

  if (username) {
    logged_in = true;
  }
</script>

<div class={hstack()}>
  <div class={css({ fontWeight: "bold", color: "amber.500", fontSize: 40 })}>
    Ponytron 🐴🤠
  </div>
  <div>
    {#if logged_in}
      <button
        class={css({ background: "amber.500", rounded: "md", p: 2 })}
        on:click={() => {
          logged_in = false;
          storedname.set("");
        }}>logout</button
      >
    {/if}
  </div>
</div>

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
{/if}

{#if $storedname}
  <div class={container()}>
    <slot />
  </div>

  <div class={css({ p: "2" })}>
    <div>Navigation:</div>
    <a href="/" class={css({ bg: "blue.500" })}>Main</a>
    <a href="/chats" class={css({ bg: "blue.500" })}>Chats</a>
  </div>
{/if}
