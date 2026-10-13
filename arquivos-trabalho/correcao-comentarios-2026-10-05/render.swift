import AppKit
import WebKit
let app = NSApplication.shared
app.setActivationPolicy(.accessory)
let path = CommandLine.arguments[1]
let out = CommandLine.arguments[2]
let width = Double(CommandLine.arguments.count > 3 ? CommandLine.arguments[3] : "390")!
let web = WKWebView(frame: NSRect(x:0,y:0,width:width,height:1600))
let window = NSWindow(contentRect: web.frame, styleMask: .borderless, backing:.buffered, defer:false)
window.contentView = web
class Delegate: NSObject, WKNavigationDelegate {
    func webView(_ view: WKWebView, didFinish navigation: WKNavigation!) {
        DispatchQueue.main.asyncAfter(deadline:.now()+1) {
            view.takeSnapshot(with:nil) { image,error in
                guard let image=image, let tiff=image.tiffRepresentation,
                      let bitmap=NSBitmapImageRep(data:tiff), let png=bitmap.representation(using:.png,properties:[:]) else {
                    print("snapshot error",String(describing:error)); exit(1)
                }
                do { try png.write(to:URL(fileURLWithPath:out)); print(out); exit(0) }
                catch { print(error); exit(1) }
            }
        }
    }
}
let delegate=Delegate()
web.navigationDelegate=delegate
web.loadFileURL(URL(fileURLWithPath:path), allowingReadAccessTo:URL(fileURLWithPath:"/Users/davisousa"))
DispatchQueue.main.asyncAfter(deadline:.now()+25) { print("render timeout"); exit(2) }
app.run()
