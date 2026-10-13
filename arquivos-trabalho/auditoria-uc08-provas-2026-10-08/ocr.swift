import Foundation
import Vision
import AppKit
for argument in CommandLine.arguments.dropFirst() {
 let url = URL(fileURLWithPath: argument)
 let request = VNRecognizeTextRequest()
 request.recognitionLevel = .accurate
 request.recognitionLanguages = ["pt-BR", "en-US"]
 request.usesLanguageCorrection = true
 do {
  try VNImageRequestHandler(url: url).perform([request])
  let text = (request.results ?? []).compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
  try text.write(to: url.deletingPathExtension().appendingPathExtension("txt"), atomically: true, encoding: .utf8)
  print(url.lastPathComponent, text.count)
 } catch { print("ERROR", argument, error) }
}
