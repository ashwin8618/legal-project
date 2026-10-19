import { useEffect, useState } from "react"

import { Button } from "@/components/ui/button"

import { fetchHello } from "./api.ts"

export function HelloPage() {
  const [message, setMessage] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false

    fetchHello()
      .then((greeting) => {
        if (!cancelled) {
          setMessage(greeting.message)
        }
      })
      .catch(() => {
        if (!cancelled) {
          setError("The API is not reachable yet.")
        }
      })

    return () => {
      cancelled = true
    }
  }, [])

  const heading = message ?? (error ? "Hello" : "Loading…")

  return (
    <main className="flex min-h-svh items-center justify-center p-6">
      <section className="w-full max-w-md rounded-xl border bg-card p-8 text-card-foreground shadow-sm">
        <p className="text-sm text-muted-foreground">Legal application</p>
        <h1 className="mt-2 text-2xl font-medium tracking-tight">{heading}</h1>
        <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
          {error ?? "The React frontend is talking to the FastAPI backend."}
        </p>
        <Button className="mt-6" variant="outline" onClick={() => window.location.reload()}>
          Refresh
        </Button>
        <p className="mt-6 font-mono text-xs text-muted-foreground">
          Press <kbd>d</kbd> to toggle dark mode
        </p>
      </section>
    </main>
  )
}
