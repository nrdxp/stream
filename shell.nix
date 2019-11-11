{ nixpkgs ? import <nixpkgs> {}, ... }:
nixpkgs.mkShell {
  buildInputs = with nixpkgs; [ python38 python38Packages.ffmpeg-python ];
}
