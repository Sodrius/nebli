import AppKit
import Foundation
let dir = URL(fileURLWithPath: CommandLine.arguments[1])
let items = try JSONSerialization.jsonObject(with: Data(contentsOf: dir.appendingPathComponent("images.json"))) as! [[String:String]]
for page in 0..<Int(ceil(Double(items.count)/12.0)) {
    let bitmap = NSBitmapImageRep(bitmapDataPlanes:nil, pixelsWide:1440, pixelsHigh:1800, bitsPerSample:8, samplesPerPixel:4, hasAlpha:true, isPlanar:false, colorSpaceName:.deviceRGB, bytesPerRow:0, bitsPerPixel:0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep:bitmap)
    NSColor.white.setFill(); NSRect(x:0,y:0,width:1440,height:1800).fill()
    for j in 0..<12 {
        let index = page*12+j
        if index >= items.count { break }
        let item = items[index], x = CGFloat(j%3)*480, y = CGFloat(3-j/3)*450
        if let img = NSImage(contentsOfFile:item["path"]!) {
            let scale = min(460/img.size.width, 385/img.size.height)
            let size = NSSize(width:img.size.width*scale,height:img.size.height*scale)
            img.draw(in:NSRect(x:x+(480-size.width)/2,y:y+45+(385-size.height)/2,width:size.width,height:size.height))
        }
        (item["label"]! as NSString).draw(in:NSRect(x:x+8,y:y+3,width:464,height:42),withAttributes:[.font:NSFont.systemFont(ofSize:16),.foregroundColor:NSColor.black])
    }
    NSGraphicsContext.restoreGraphicsState()
    try bitmap.representation(using:.png,properties:[:])!.write(to:dir.appendingPathComponent("contact-\(page).png"))
}
