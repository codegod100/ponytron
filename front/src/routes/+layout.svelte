<script>
  export let data;
  import "../app.css";
  import { css } from "styled-system/css";
  import { container, hstack } from "styled-system/patterns";
  import ponylog from "$lib/ponylog";

  ponylog();
</script>

<div class={hstack()}>
  <div class={css({ fontWeight: "bold", color: "amber.500", fontSize: 40 })}>
    Ponytron 🐴🤠
  </div>
  <div>
    {#if data.username}
      <form method="POST">
        <button
          name="username"
          value=""
          type="submit"
          class={css({ background: "amber.500", rounded: "md", p: 2 })}
          on:click={() => {}}>logout</button
        >
      </form>
    {/if}
  </div>
</div>

{#if !data.username}
  <form method="POST">
    Username
    <input
      name="username"
      type="text"
      class={css({ background: "amber.500", rounded: "md", p: 2 })}
    />
    Password
    <input
      type="text"
      class={css({ background: "amber.500", rounded: "md", p: 2 })}
    />
    <button class={css({ bg: "amber.500", rounded: "md", p: 2 })}>login</button>
  </form>
{/if}

{#if data.username}
  <div class={container()}>
    <slot />
  </div>

  <div class={css({ p: "2" })}>
    <div>Navigation:</div>
    <a href="/" class={css({ bg: "blue.500" })}>Main</a>
    <a href="/chats" class={css({ bg: "blue.500" })}>Chats</a>
  </div>
{/if}
