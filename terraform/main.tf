provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "trusty-solution-240102"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}
resource "google_compute_instance" "tf_instance" {
  name         = "tf-instance-${count.index}"
  machine_type = "n1-standard-1"
  count        = 1


  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20190530"
      size  = 30
    }
  }
  metadata = {
    sshKeys = "pop:${file("~/.ssh/hitme.pub")}"
  }

  network_interface {
    network = "default"
    access_config {}
  }

  tags = ["my-web"]
}
output "ip" {
  value = "${google_compute_instance.tf_instance.*.network_interface.0.access_config.0.nat_ip}"
}