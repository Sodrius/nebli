import AppKit
import WebKit
import Foundation

final class Renderer: NSObject, WKNavigationDelegate {
    let web: WKWebView
    let window: NSWindow
    let root: URL
    var jobs: [[String:Any]]
    var active: [String:Any] = [:]
    init(_ root:URL) throws {
        self.root=root
        self.jobs=try JSONSerialization.jsonObject(with:Data(contentsOf:root.appendingPathComponent("render-jobs.json"))) as! [[String:Any]]
        web=WKWebView(frame:NSRect(x:0,y:0,width:820,height:1100))
        window=NSWindow(contentRect:web.frame,styleMask:[.borderless],backing:.buffered,defer:false)
        super.init()
        web.navigationDelegate=self
        window.contentView=web
        window.orderBack(nil)
    }
    func next() {
        if jobs.isEmpty {NSApplication.shared.stop(nil);exit(0)}
        active=jobs.removeFirst()
        let width=active["width"] as! Int
        web.setFrameSize(NSSize(width:width,height:1100))
        window.setContentSize(web.frame.size)
        let path=root.appendingPathComponent(active["html"] as! String)
        web.loadFileURL(path,allowingReadAccessTo:URL(fileURLWithPath:"/"))
    }
    func webView(_ webView:WKWebView,didFinish navigation:WKNavigation!) {
        DispatchQueue.main.asyncAfter(deadline:.now()+0.8) {
            self.web.evaluateJavaScript("JSON.stringify({scrollWidth:document.documentElement.scrollWidth,width:innerWidth,titleColor:document.getElementById('title')?getComputedStyle(document.getElementById('title')).color:null,images:[...document.querySelectorAll('img')].filter(x=>x.offsetWidth>0).map(x=>({src:x.getAttribute('src'),width:x.offsetWidth,height:x.offsetHeight,loaded:x.complete&&x.naturalWidth>0})),text:document.body.innerText})") { result,error in
                let name=self.active["name"] as! String
                if let value=result as? String {try? value.write(to:self.root.appendingPathComponent(name+".json"),atomically:true,encoding:.utf8)}
                self.web.takeSnapshot(with:nil) {img,error in
                    if let data=img?.tiffRepresentation,let bitmap=NSBitmapImageRep(data:data),let png=bitmap.representation(using:.png,properties:[:]) {
                        try? png.write(to:self.root.appendingPathComponent(name+".png"))
                        print(name)
                    } else {fputs("Snapshot failed: \(String(describing:error))\n",stderr);exit(1)}
                    self.next()
                }
            }
        }
    }
}
let app=NSApplication.shared
app.setActivationPolicy(.accessory)
let renderer=try Renderer(URL(fileURLWithPath:CommandLine.arguments[1]))
renderer.next()
app.run()
