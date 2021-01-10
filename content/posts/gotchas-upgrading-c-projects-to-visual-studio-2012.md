+++
author = "Batista Harahap"
categories = ["c", "gotchas", "metro", "microsoft", "rtm", "windows 8", "xaml"]
date = 2012-10-08T16:35:54Z
description = ""
draft = false
slug = "gotchas-upgrading-c-projects-to-visual-studio-2012"
tags = ["c", "gotchas", "metro", "microsoft", "rtm", "windows 8", "xaml"]
title = "Gotchas Upgrading C# Projects to Visual Studio 2012"

+++


My previous post is about my experience developing for Windows 8 RTM using Visual Studio 2012, there were BREAKING changes with Visual Studio 2012 and I feel obliged to map my own efforts for the benefit of other developers. So I'm going straight to the topic. Most of the content is NOT from my own experience, I put them down here to compile the gotchas.

Everything you see here is actually available as a whitepaper published by Microsoft <a href="http://www.microsoft.com/en-us/download/details.aspx?id=30706" target="_blank">here</a>.

From Shai Raiten's excellent guide <a href="http://blogs.microsoft.co.il/blogs/shair/archive/2012/06/03/upgrade-metro-app-from-beta-to-rc.aspx" target="_blank">here</a>, find and replace all namespaces found below to the value on its right:
<table cellspacing="0" cellpadding="2">
<tbody>
<tr>
<td valign="top">Type</td>
<td valign="top">Old Value</td>
<td valign="top">New Value</td>
<td valign="top">Comment</td>
</tr>
<tr>
<td valign="top">Class</td>
<td valign="top">PointerEventArgs</td>
<td valign="top">PointerRoutedEventArgs</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">FocusVisualBlackStrokeBrush</td>
<td valign="top">FocusVisualBlackStrokeThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">FocusVisualWhiteStrokeBrush</td>
<td valign="top">FocusVisualWhiteStrokeThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ApplicationHoverTextBrush</td>
<td valign="top">ApplicationPointerOverForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ApplicationPressedTextBrush</td>
<td valign="top">ApplicationPressedForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ControlDisabledTextBrush</td>
<td valign="top">ButtonDisabledForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ApplicationSecondaryTextBrush</td>
<td valign="top">ApplicationSecondaryForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemForegroundBrush</td>
<td valign="top">AppBarItemForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemBackgroundBrush</td>
<td valign="top">AppBarItemBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemHoverBackgroundBrush</td>
<td valign="top">AppBarItemPointerOverBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemHoverForegroundBrush</td>
<td valign="top">AppBarItemPointerOverForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemForegroundBrush</td>
<td valign="top">AppBarItemForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemPressedForegroundBrush</td>
<td valign="top">AppBarItemPressedForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">AppBarItemDisabledForegroundBrush</td>
<td valign="top">AppBarItemDisabledForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonBackgroundBrush</td>
<td valign="top">BackButtonBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonGlyphBrush</td>
<td valign="top">BackButtonForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonPressedGlyphBrush</td>
<td valign="top">BackButtonPressedForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonHoverBackgroundBrush</td>
<td valign="top">BackButtonPointerOverBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonHoverGlyphBrush</td>
<td valign="top">BackButtonPointerOverForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">BackButtonGlyphBrush</td>
<td valign="top">BackButtonForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ListViewItemPlaceholderRectBrush</td>
<td valign="top">ListViewItemPlaceholderBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ListViewItemOverlayBackgroundBrush</td>
<td valign="top">ListViewItemOverlayBackgroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ListViewItemOverlayTextBrush</td>
<td valign="top">ListViewItemOverlayForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Style</td>
<td valign="top">ListViewItemOverlaySecondaryTextBrush</td>
<td valign="top">ListViewItemOverlaySecondaryForegroundThemeBrush</td>
<td valign="top"></td>
</tr>
<tr>
<td valign="top">Method</td>
<td valign="top">this.Dispatcher.InvokeAsync(</td>
<td valign="top">this.Dispatcher.RunAsync</td>
</tr>
</tbody>
</table>
My own additions:
<table cellspacing="0" cellpadding="2">
<tbody>
<tr>
<td valign="top">Type</td>
<td valign="top">Old Value</td>
<td valign="top">New Value</td>
</tr>
<tr>
<td valign="top">XAML</td>
<td valign="top">VerticalScrollMode="Rails"</td>
<td valign="top">IsVerticalRailEnabled="True"</td>
</tr>
</tbody>
</table>
If you also wanna help with your experience, please leave a comment and I will update the list accordingly.