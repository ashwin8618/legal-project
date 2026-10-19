import { render, screen } from "@testing-library/react"
import { afterEach, describe, expect, it, vi } from "vitest"

import { HelloPage } from "./HelloPage.tsx"

describe("HelloPage", () => {
  afterEach(() => {
    vi.restoreAllMocks()
  })

  it("shows the greeting returned by the API", async () => {
    vi.spyOn(globalThis, "fetch").mockResolvedValue(
      new Response(JSON.stringify({ message: "Hello, world" }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }),
    )

    render(<HelloPage />)

    expect(
      await screen.findByRole("heading", { name: "Hello, world" }),
    ).toBeInTheDocument()
  })
})
