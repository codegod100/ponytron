<script>
  import Login from "$lib/Login.svelte";
  export let data;
  console.log("layout data", data);
  import { storedname } from "$lib/common";
  import "../app.css";
  import { css } from "styled-system/css";
  import { container } from "styled-system/patterns";
  import { PUBLIC_API, PUBLIC_WEBSOCKET } from "$env/static/public";
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
</script>

<h1 class={css({ fontWeight: "bold", color: "amber.500", fontSize: 40 })}>
  Ponytron 🐴
</h1>

<Login />
{#if $storedname}
  <div class={container()}>
    <slot />
  </div>
{/if}

<div class={css({ p: "2" })}>
  <div>Navigation:</div>
  <a href="/" class={css({ bg: "blue.500" })}>Main</a>
  <a href="/chats" class={css({ bg: "blue.500" })}>Chats</a>
</div>
