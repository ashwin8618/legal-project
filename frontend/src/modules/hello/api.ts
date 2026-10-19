export type HelloResponse = {
  message: string
}

export async function fetchHello(): Promise<HelloResponse> {
  const response = await fetch("/api/v1/hello")
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`)
  }
  return response.json() as Promise<HelloResponse>
}
