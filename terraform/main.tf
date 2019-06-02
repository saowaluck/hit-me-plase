provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "trusty-solution-240102"
  region      = "asia-southeast1"
  zone        = "asia-southeast-b"
}
